<template>
  <div>
    <div id="student-card" :style="{width: '300px', paddingLeft: '10px', paddingRight: '10px', fontSize: '14px', margin: 'auto'}">
      <div :style="{margin: 'auto'}">
        <div :style="{margin: 'auto', display: 'flex', flexDirection: 'column'}">
          <img :style="{margin: 'auto'}" :src="nstu_logo" height="80" width="60"/>
          <div :style="{display: 'flex', justifyContent: 'center'}">
            <h2 :style="{fontSize: '12px'}">Noakhali Science and Technology University</h2>
          </div>
          
        </div>
      </div>
      <div :style="{display: 'flex', flexDirection: 'column', justifyContent: 'center'}">
        <p :style="{fontSize: '12px', margin: 0}">Name: {{ student.full_name }}</p>
        <p :style="{fontSize: '12px', margin: 0}">Student ID: {{ student.student_id }}</p>
        <p :style="{fontSize: '12px', margin: 0}">Batch: {{ student.batch ? student.batch.name : '' }}</p>
      </div>
      <div :style="{padding: '10px'}">
        <img :src="this.qr_code_base64" height="100px" width="100px"/>
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

<style scoped>

</style>