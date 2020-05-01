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
        <!-- <p class="leading-normal text-md text-gray-650">
            Found on GitHub
        </p> -->
        </header>
        <p class="mt-2 text-md text-gray-700 leading-normal">
        An example of a web application that leverages distributed systems technologies.
        </p>
        <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
            <li class="rounded-full px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                NuxtJS
            </li>
    
        </ul>
    </section>
</template>

<script>
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
                axios.get('api/description',{
                    params: {
                    repo: name
                    }
                })
                .then(response => {
                    this.track = response.data.curr
                    console.log(response);
                })
                .catch(error => {
                    console.log(response);
                    console.log(error)
                })
            }
        }, created () {
            this.getDescription(),
            this.getDescriptionFromBackend()
    },
    props: [
        'name',
    ]
}
</script>