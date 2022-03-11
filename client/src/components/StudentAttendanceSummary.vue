<template>
<div style="background-color: #202C46">
    <v-data-table
      :headers="headers"
      :items="attendances"
      item-key="course_title"
      class="elevation-1"
      :search="search"
    >
      <template v-slot:top>
        <v-text-field
          v-model="search"
          label="Search Course"
          class="mx-4"
        ></v-text-field>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "StudentAttendanceSummary",
  props: {
    attendances: {
      type: Array,
      default: () => [],
      required: false
    }
  },
  data(){
    return {
      search: '',
    }
  },
  computed: {
    headers () {
      return [
        {
          text: 'Course Title',
          align: 'start',
          value: 'course_title',
          filter: value => {
            if (!this.course_title) return true

            return value < this.course_title
          },
        },
        {
          text: 'Total Class',
          value: 'total_class',
          filter: value => {
            if (!this.total_class) return true

            return value < parseInt(this.total_class)
          },
        },
        {
          text: 'Class Attended',
          value: 'total_present',
          filter: value => {
            if (!this.total_present) return true

            return value < parseInt(this.total_present)
          },
        },
        {
          text: 'Percentage(%)',
          value: 'percentage',
          filter: value => {
            if (!this.percentage) return true

            return value < parseFloat(this.percentage)
          },
        },
      ]
    },
  },
  methods: {
    filter_search(value, search, item){
      console.log(value, search, item);
      return false;
    
    }
  }
}
</script>

<style scoped lang="scss">
table {

}
tr:nth-child(2) {
    background-color: red;
  }
</style>