<template>
  <GenericView
      title="Batch"
      :data="batches"
      :headers="headers"
      @delete="delete_batch"
  >
    <template #edit-data="edit_data">
      <batchForm :key="Math.random()" :data="edit_data.edit_item" :update_data="Boolean(edit_data.edit_item.id)"/>
    </template>
    <template #delete-data="{delete_item}">
      <batchForm :key="Math.random()" :data="delete_item" :update_data="true" :view_only="true" />
    </template>
  </GenericView>
</template>

<script>
import GenericView from "./GenericView";
import BackendApi from "../js/backend";
import BatchForm from "../components/forms/BatchForm";
import batch_mixin from "../mixins/Batch";

export default {
  name: "BatchView",
  components: {BatchForm, GenericView},
  mixins: [batch_mixin],
  methods: {
    delete_batch(item) {
      return BackendApi.batch.delete(item.id)
          .then(res => {
            console.log(res);
            this.success = true;
          }).catch(err => {
            console.error(err);
          }).finally(() => this.show_confirm = true);
  }
}
,
data: function () {
  return {
    headers: [
      {text: 'Name', value: 'name', align: "start"},
      {text: 'Active', value: 'active'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
  }
}

}
</script>