<template>
  <div class="home">
    <Header/>
    <StudentForm />
    <button @click="success">Refresh</button>
    <QRCodeReader :camera="camera" @success="success" />
  </div>
</template>

<script>
import StudentForm from "../components/forms/StudentForm";
import QRCodeReader from "../components/QRCodeReader";
import Header from "../components/Header";
export default {
  name: "Home",
  components: {
    Header,
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
