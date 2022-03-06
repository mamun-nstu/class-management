<template>
  <div class="home">
      <v-carousel mx-10>
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i"
          :src="item.src"
          reverse-transition="fade-transition"
          transition="fade-transition"
        >
        </v-carousel-item>
      </v-carousel>
    <StudentForm />
    <button @click="success">Refresh</button>
    <QRCodeReader :camera="camera" @success="success" />
  </div>
</template>

<script>
import StudentForm from "../components/forms/StudentForm";
import QRCodeReader from "../components/QRCodeReader";

export default {
  name: "Home",
  components: {
    QRCodeReader,
    StudentForm,
  },

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

<style scoped></style>
