<template>
  <FormContainer
      :url="'/api/batches/'"
      :data="batch"
      :key="data.id"
      :method="update_data ? 'put': 'post'"
  >
    <template #form>
      <div class="batch register">
        <TextField
            label="Name"
            v-model="batch.name"
            :rules="{required: true}"
        />

        <v-checkbox dark label="Active" v-model="batch.active"/>

      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from "./FormContainer";
import TextField from "../elements/TextField";
import _ from 'lodash';

export default {
  name: "BatchForm",
  components: {
    TextField,
    FormContainer,
  },
  props: {
    data: {
      type: Object,
      required: false,
      default: () => {
      }
    },
    view_only: {
      type: Boolean,
      required: false,
      default: false
    },
    // whether data should be created or updated
    update_data: {
      type: Boolean,
      required: false,
      default: false,
    }
  },
  mounted() {
    this.batch = _.cloneDeep(this.data) || {};
  },
  data: function () {
    return {
      batch: {},
    }
  }
};
</script>

