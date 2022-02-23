<template>
  <div class="student-attendance">
    <v-row class="align-center">
      <v-col class="col-2">
        <p>{{ attendance_data.student.student_id }}</p>
      </v-col>
      <v-col class="col-4">
        <p>{{ attendance_data.student.full_name }}</p>
      </v-col>
      <v-col class="col-2">
        <v-checkbox
            v-model="present"
            @change="$emit('change', {id: attendance_data.student.id, value: present})">
        </v-checkbox>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: "StudentAttendance",
  props: {
    attendance_data: {
      type: Object,
      required: true
    }
  },
  beforeUpdate() {
    this.present = this.attendance_data.present;
  },
  beforeMount() {
    this.present = this.attendance_data.present;
  },
  data() {
    return {
      present: false
    }
  }
}
</script>

<style scoped>

</style>