<template>
  <div class="home">
    HOme page
    <StudentForm />
  </div>
</template>

<script>
import StudentForm from "../components/forms/StudentForm";
export default {
  name: "Home",
  components: {StudentForm},
};
</script>

<style scoped></style>
