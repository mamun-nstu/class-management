<template>
  <div class="crud-view">
    <v-data-table
      class="elevation-1"
      :headers="headers"
      :items="data"
      sort-by="first_name"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>{{ title }}</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="750px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                New {{ title }}
              </v-btn>
            </template>
            <v-card color="#202C46" style="opacity: .9" rounded>
              <slot name="edit-data" v-bind:edit_item="editedItem"></slot>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="750px">
            <v-card color="#202C46" style="opacity: .9">
              <v-card-title class="text-h5 white--text text-center"><p style="margin: auto">Are you sure you want to delete this item?</p>
              </v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <slot name="delete-data" v-bind:delete_item="itemToDelete"></slot>
                <v-spacer></v-spacer>
              </v-card-actions>
              <div class="d-flex justify-center">
                <v-btn style="width: 150px; background-color: #FFFFFF; color: black"  class="px-10 mx-10 my-10" text @click="closeDelete">Cancel</v-btn>
                <v-btn style="width: 150px; background-color: red; color: white" class="px-10 mx-10 my-10" text @click="deleteItemConfirm">OK</v-btn>
              </div>
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
  </div>
</template>

<script>

export default {
  name: "GenericView",
  props: {
    data: {
      type: Array,
      required: false,
      default: () => []
    },
    headers: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  },
  
  data: function () {
    return {
      dialog: false,
      dialogDelete: false,
      editedIndex: -1,
      editedItem: {},
      defaultItem: {},
      itemToDelete: {},
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
      this.itemToDelete = Object.assign({}, item)
      this.dialogDelete = true
    },
    
    deleteItemConfirm() {
      this.$emit('delete', this.itemToDelete);
      this.closeDelete();
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
        this.itemToDelete = {};
      })
    }
  }
  
}
</script>

<style scoped lang="scss">
.crud-view {
  max-width: 900px;
  width: 100%;
  margin: auto;
}
</style>