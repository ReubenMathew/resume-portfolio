<template>
    <section class="mb-4 break-inside-avoid">
        <header>
        <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
            <a href="https://github.com/ReubenMathew/DistributedSystemsPortfolio" class="group">
            {{name}}
            <span
                class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
            </a>
        </h3>
        </header>
        <p class="mt-2 text-md text-gray-700 leading-normal">
            {{description}}
        </p>
        <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
            <li v-for="topic in topics" v-bind:key="topic" class="rounded-full px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                {topic}
            </li>
        </ul>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    data () {
            return {
                description: '',
                topics: [],
            }
        }, methods: {
            getDescription() {
                this.description = this.getDescriptionFromBackend()
            },
            getDescriptionFromBackend() {
                axios.get('/api/description',{
                    params: {
                        repo: this.name
                    }
                })
                .then((response) => {
                    this.description = response.data.result
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error)
                })
            },
            getTopicsFromBackend() {
                axios.get('/api/topics',{
                    params: {
                        repo: this.name
                    }
                })
                .then((response) => {
                    this.topics = response.data.result
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error)
                })
            }
            
        }, created () {
            this.getDescription(),
            this.getDescriptionFromBackend(),
            this.getTopics(),
            this.getTopicsFromBackend()
    },
    props: [
        'name',
    ]
}
</script>