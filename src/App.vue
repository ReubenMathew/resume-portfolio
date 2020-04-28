<template>
  <div class="font-firago hyphens-manual">
    <div class="p-6 mx-auto page max-w-2xl print:max-w-letter md:max-w-letter md:h-letter xsm:p-8 sm:p-9 md:p-16 bg-white">
      
      <!-- Based on template from https://github.com/WebPraktikos/universal-resume -->

      <!-- Name -->
      <Name/>

<!-- Column -->
      <div class="md:col-count-2 print:col-count-2 col-gap-md md:h-letter-col print:h-letter-col col-fill-auto">
        <!-- Use mt-3 class when the element isn’t the first one in the column -->
        
        <About/>
        <Experience/>
        <Education/>
        <Leadership/>
        <Projects/>
        <Contact/>
        
      </div>
      <!-- end Column -->



    </div>
  </div>
</template>

<script>

import Name from './components/Name'
import About from './components/About'
import Experience from './components/Experience'
import Education from './components/Education'
import Leadership from './components/Leadership'
import Projects from './components/Projects'
import Contact from './components/Contact'

export default {
  name: 'App',
  components: {
    Name,
    About,
    Experience,
    Education,
    Leadership,
    Projects,
    Contact,
  },
}
</script>