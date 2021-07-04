<template>
  <v-data-table
      class="elevation-1"
      :headers="headers"
      :items="students"
      sort-by="first_name"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
            class="mx-4"
            inset
            vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
            v-model="dialog"
            max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
            >
              New Student
            </v-btn>
          </template>
          <v-card>
            <StudentForm :student_data="editedItem"/>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
          small
          @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import {UPDATE_STUDENTS} from "../store/mutation_types";
import StudentForm from "../components/forms/StudentForm";

export default {
  name: "StudentView",
  components: {StudentForm},
  created() {
    this.$store.dispatch(UPDATE_STUDENTS);
  },
  computed: {
    students() {
      return this.$store.state.students.data;
    }
  },
  data: function () {
    return {
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'Student ID',
          align: 'start',
          value: 'student_id',
        },
        {text: 'Email Address', value: 'username'},
        {text: 'First Name', value: 'first_name'},
        {text: 'Last Name', value: 'last_name'},
        {text: 'Actions', value: 'actions', sortable: false},
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {},
      defaultItem: {},
    }
  },
  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },
  methods: {
    editItem(item) {
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = {};
      })
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = {};
      })
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem)
      } else {
        this.desserts.push(this.editedItem)
      }
      this.close();
    },
  }

}
</script>

<style scoped>

</style>