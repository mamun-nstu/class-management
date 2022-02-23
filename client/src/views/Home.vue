<template>

  <div class="home">
    <v-carousel>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
    </v-carousel>

    ICE Attendance Management System
    <StudentForm />
  </div>
</template>

<script>
import StudentForm from "../components/forms/StudentForm";
export default {
  name: "Home",
  components: {StudentForm},
  data () {
      return {
        items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
          {
            src: '@/assets/slider2.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          },
        ],
      }
    },
};
</script>

<style scoped></style>
