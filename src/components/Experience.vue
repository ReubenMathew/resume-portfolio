<template>
    <section class="mt-8">
        <!-- To keep in the same column -->
        <div class="break-inside-avoid">
        <h2 class="mb-4 font-bold tracking-widest text-sm2 text-gray-550 print:font-normal">
            EXPERIENCE
        </h2>
        </div>

        <section class="mb-4 break-inside-avoid">
        <header>
            <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
            Royal Bank of Canada (RBC)
            </h3>
            <p class="leading-normal text-md text-gray-650">
            Apr 2019 – Aug 2019 | Data Scientist (Intern)
            </p>
        </header>
        
        <ul class="">

            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
            Automated data loading and cleaning processes
            </li>

            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
                Extracted <b>500gb</b> of unstructured data from legacy files,<br>
                The data was cleansed and enriched with existing data sources for the purpose of
                validation and governance
            </li>
            
            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
                Presented a dashboard displaying visual, statistical and 
                geographic insights on the newly extracted dataset to Senior Management
            </li>

            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
                Worked under Agile/SCRUM Methodologies and utilized tools such as JIRA, Enterprise GitHub and Confluence
            </li>

            <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed"> 
                <li v-for="tag in tags" v-bind:key="tag" class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                    {{tag}}
                </li>              
            </ul>

        </ul>
        </section>

        <section class="mb-4 break-inside-avoid">
        <header>
            <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
            <a href="https://www.stem1.ca/" class="group">
                STEM1
                <span
                class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
            </a>
            </h3>
            <p class="leading-normal text-md text-gray-650">
            Jun 2018 – Aug 2018 | Computer Science Instructor
            </p>
        </header>
        <ul class="">
            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
            Taught computer programs, algorithms and computer design to students (K-12)
            </li>
            <li class="mt-2 text-md text-gray-700 leading-normal">
            <span class="absolute -ml-3 sm:-ml-3.2 select-none transform -translate-y-px">›</span>
            Created and implemented a beginner’s curriculum focused on robotics
            </li>
        </ul>
        </section>

    </section>

</template>

<script>
export default {
    data: () => ({
        tags: [
            'Python',
            'Tableau',
            'SQL',
            'Bash',
            'R',
            'Java',
        ]
    })
}
</script>