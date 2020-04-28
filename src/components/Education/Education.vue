<template>
    <div>
        <div v-if="schools">
            <h2 class="mb-4 font-bold tracking-widest text-sm2 text-gray-550 print:font-normal">
                EDUCATION
            </h2>
        
            <div v-for="school in schools" v-bind:key="school"> 
                <EducationCard :school="school"/>
            </div>
        </div>

    </div>
</template>

<script>
import EducationCard from './EducationCard'

export default {
    components : {
        EducationCard,
    },
    data: () => ({
        schools: [
            {
                name: 'York University',
                program: 'Software Engineering',
                from: '2018',
                to: 'Current',
                degree: 'Bachelor of Engineering'
            },
            {
                name: 'Chinguacousy Secondary School',
                program: 'Sci-Tech',
                from: '2014',
                to: '2018',
                degree: 'Highschool Diploma'
            }
        ]
    })
}
</script>