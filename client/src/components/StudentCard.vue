<template>
  <div>
    <div id="student-card" class="student-card">
      <div class="text-center ">
        <div class="nstu-logo mt-2 mb-2">
          <img :src="nstu_logo"/>
        </div>
        <div>
          <h2>Noakhali Science and Technology University</h2>
        </div>
      </div>
      <div class="text-center">
        <p>Name: {{ student.full_name }}</p>
        <p>Student ID: {{ student.student_id }}</p>
        <p>Batch: {{ student.batch ? student.batch.name : '' }}</p>
      </div>
      <div class="qr-img-container text-center">
        <img :src="this.qr_code_base64" class="qr-img"/>
      </div>
    </div>
  </div>
</template>

<script>
import nstu_logo from '@/assets/nstu-logo.jpg';

export default {
  name: "StudentCard",
  props: {
    qr_code_base64: {
      type: String,
      required: true
    },
    student: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      nstu_logo,
    }
  }
}
</script>

<style scoped lang="scss">
.student-card {
  width: 300px;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 1px;
  margin: auto;
  
  .nstu-logo {
    display: flex;
    justify-content: center;
    
    img {
      height: 80px;
      width: 60px;
    }
  }
  
  
  .qr-img-container {
    padding-top: 10px;
    
    img.qr-img {
      height: 100px;
      width: 100px;
    }
  }
  
  h2 {
    font-size: 13px;
  }
  
  p {
    font-size: 12px;
    margin: 0;
    padding: 0;
  }
}
</style>