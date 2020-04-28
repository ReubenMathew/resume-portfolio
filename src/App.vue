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


        <section class="mt-8">

          <!-- To keep in the same column -->
          <div class="break-inside-avoid">

            <h2 class="mb-4 font-bold tracking-widest text-sm2 text-gray-550 print:font-normal">
              PROJECTS
            </h2>

            <section class="mb-4 break-inside-avoid">
              <header>
                <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
                  <a href="https://github.com/ReubenMathew/DistributedSystemsPortfolio" class="group">
                    Distributed Systems Portfolio
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
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  NuxtJS
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Figma
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Python
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Flask
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Redis
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Axios
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Gunicorn
                </li>  
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Kubernetes
                </li>  
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Docker
                </li> 
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Postman
                </li>      
              </ul>
            </section>

          </div>

          <section class="mb-4 break-inside-avoid">
            <header>
              <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
                <a href="https://github.com/ReubenMathew/DocScanner" class="group">
                  DocScanner
                  <span
                    class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                </a>
              </h3>
              <!-- <p class="leading-normal text-md text-gray-650">
                Found on GitHub
              </p> -->
            </header>
            <p class="mt-2 text-md text-gray-700 leading-normal">
              A simple web application based document scanner utilizing an OpenCV Edge Detection Engine.
            </p>
            <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Python
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Flask
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  OpenCV
                </li>
                <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                  Numpy
                </li>
              </ul>
          </section>

          <section class="mb-4 break-inside-avoid">
            <header>
              <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
                <a href="https://github.com/ReubenMathew/DataOpsExperiments" class="group">
                  Machine Learning Experiments
                  <span
                    class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                </a>
              </h3>
              <!-- <p class="leading-normal text-md text-gray-650">
                Found on GitHub
              </p> -->
            </header>
            <p class="mt-2 text-md text-gray-700 leading-normal">
              Exploration and practice with various machine learning techniques and tools.
            </p>
            <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                PyTorch
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                NLP
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                Scikit-learn
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                Tensorflow
              </li>
            </ul>
          </section>

          <section class="mb-4 break-inside-avoid">
            <header>
              <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
                <a href="https://github.com/EECS2311-Team8/SoftwareDevelopmentProject" class="group">
                  VennFX
                  <span
                    class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                </a>
              </h3>
              <!-- <p class="leading-normal text-md text-gray-650">
                Found on GitHub
              </p> -->
            </header>
            <p class="mt-2 text-md text-gray-700 leading-normal">
              Desktop application of a customizable venn diagram maker.
            </p>
            <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                Java
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                JavaFX
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                CircleCI
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                Gradle
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                JUnit
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                TestFX 
              </li>
            </ul>
          </section>

          <section class="mb-4 break-inside-avoid">
            <header>
              <h3 class="text-lg font-semibold text-gray-700 leading-snugish">
                <a href="https://business-template.now.sh/" class="group">
                  Business Frontend Template
                  <span
                    class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                </a>
              </h3>
              <!-- <p class="leading-normal text-md text-gray-650">
                Found on GitHub
              </p> -->
            </header>
            <p class="mt-2 text-md text-gray-700 leading-normal">
              A modern web template meant for businesses or financial firms.
            </p>
            <ul class="my-2 mb-6 flex flex-wrap text-md leading-relaxed">
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                JavaScript
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                VueJS
              </li>
              <li class="px-3 mr-2 mt-2 text-base text-gray-750 print:bg-white print:border-inset bg-gray-200">
                TailwindCSS
              </li>
            </ul>
          </section>


        </section>



        <section class="mt-8">

          <!-- To keep in the same column -->
          <div class="break-inside-avoid">

            <h2 class="mb-4 font-bold tracking-widest  text-sm2 text-gray-550 print:font-normal">
              CONTACT
            </h2>

            <section class="mb-4 break-inside-avoid">
              <ul class="list-inside pr-7">
                <li class="mt-2 leading-normal text-gray-700 text-md">
                  <a href="//reubenninan.tech" class="group">
                      reubenninan.tech
                    <span
                      class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                  </a>
                </li>
                <li class="mt-2 leading-normal text-gray-700 text-md">
                  <a href="//twitter.com/NinanReuben" class="group">
                    twitter.com/NinanReuben
                    <span
                      class="inline-block text-gray-550 print:text-black font-normal group-hover:text-gray-700 transition duration-100 ease-in">↗</span>
                  </a>
                </li>
                <li class="mt-2 leading-normal text-gray-700 text-md">
                  Toronto, Ontario
                </li>
                <li class="mt-2 leading-normal text-gray-700 text-md">
                  reubenninan@outlook.com
                </li>
              </ul>
            </section>

          </div>

        </section>

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

export default {
  name: 'App',
  components: {
    Name,
    About,
    Experience,
    Education,
    Leadership,
  },
}
</script>