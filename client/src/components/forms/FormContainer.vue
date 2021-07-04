<template>
  <div class="form-container">
    <div class="d-flex flex-column">
      <v-alert
          v-model="show_confirm"
          border="left"
          close-text="Close Alert"
          :color="success? 'success': 'danger'"
          dark
          dismissible
      > {{ success ? 'Success' : 'Error occurred' }}
      </v-alert>
      <ValidationObserver v-slot="{invalid}" slim>
        <slot name="form"></slot>
        <v-btn class="btn-primary" :disabled="invalid" @click="submit"> Submit</v-btn>
      </ValidationObserver>
    </div>

  </div>
</template>

<script>
import {ValidationObserver} from 'vee-validate';
import BackendApi from '../../js/backend';

export default {
  name: "FormContainer",
  components: {
    ValidationObserver
  },
  props: {
    url: {
      type: String,
      required: true
    },
    method: {
      type: String,
      required: false,
      default: 'post'
    },
    data: {
      type: Object,
      required: false,
      default: () => {
      }
    }
  },
  data: function () {
    return {
      show_confirm: false,
      success: false
    }
  },
  methods: {
    submit() {
      console.log('Submitting to ' + this.url);
      const app = this;
      let backend_url = app.url;
      if (app.data.id) {
        backend_url = `${app.url}/${app.data.id}/`;
      }
      return BackendApi.generic.send({
        url: backend_url,
        method: this.method,
        data: app.data
      })
          .then(res => {
            console.log(res);
            this.success = true;
          }).catch(err => {
            console.error(err);
          }).finally(() => this.show_confirm = true);
    }
  }
}
</script>

<style scoped>

</style>