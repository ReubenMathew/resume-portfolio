<template>
    <section class="mb-4 break-inside-avoid">
        <header>
        <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
            {{school.name}} - {{school.program}}
        </h3>
        <p class="leading-normal text-md text-gray-650">
            {{school.from}} – {{school.to}} | {{school.degree}}
        </p>
        </header>
    </section>
</template>

<script>


export default {
    props: ['school']
}
</script>