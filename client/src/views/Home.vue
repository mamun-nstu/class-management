<template>
  <div class="home">

    <v-carousel show-arrows-on-hover  cycle interval="3000" class="text-center ma-auto" height="450" width="30" style="width: 1100px; border-radius: 20px; align-content: center;">
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      >
      </v-carousel-item>
    </v-carousel>

    <v-img class="white--text mt-16 text-center text-capitalize" src="@/assets/bg1.jpg" height="700">
      <div class="mt-16">
        <p class="text-h3">
          <span>Welcome</span> <br>to <br><span>ICE Attendance Management System</span>
        </p>
        <p class="text-h4 mt-16 text-decoration-underline">
          Here You can :
        </p>

        <v-container class="blue  white--text text-h3" style="margin-top: 100px; border-radius: 4px;" >
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab alias aliquid,

        </v-container>

      </div>



    </v-img>




    <div class=" " style="height: 350px; background: #202C46;">
      <v-row  class="" style="margin-left: 200px;">
        <v-col class="col-md-4 full-height mt-11">
          <p >
            <span class="white--text text-h5 ml-11" >Total</span>  <br> <span class="white--text text-h5 ml-4" >Instructors</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            14
          </v-avatar>
        </v-col>

        <v-col class="col-md-4 full-height mt-11">
          <p >
            <span class="white--text text-h5 ml-10" >Total</span>  <br> <span class="white--text text-h5 ml-6" >Students</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            765
          </v-avatar>
        </v-col>

        <v-col class="col-md-4 full-height mt-11">
          <p >
            <span class="white--text text-h5 ml-10" >Total</span>  <br> <span class="white--text text-h5 ml-6" >Courses</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            44
          </v-avatar>
        </v-col>

      </v-row>

    </div>




  </div>
</template>

<script>


export default {
  name: "Home",
  data(){
    return {
      camera: 'auto',
      items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
        ],
    }
  },
  methods: {
    success() {
      this.camera = 'off';
      this.$nextTick(() => {
        this.camera = 'auto';
      })
    }
  },
};
</script>

<style scoped>

</style>
