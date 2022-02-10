<template>
  <div class="home">
    HOme page
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
