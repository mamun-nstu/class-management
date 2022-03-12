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
      <ValidationObserver v-slot="{invalid, handleSubmit}" slim>
        <slot name="form"></slot>
        <v-btn class="btn-primary" @click="handleSubmit(submit)"> Submit</v-btn>
      </ValidationObserver>
    </div>
  </div>
</template>

<script>
import {ValidationObserver} from 'vee-validate';
import BackendApi from '../../js/backend';
import _ from 'lodash';

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
    async submit() {
      console.log('Submitting to ' + this.url);
      const app = this;
      let backend_url = app.url;
      if (app.data.id) {
        backend_url = `${app.url}/${app.data.id}/`;
      }
      const req_data = _.cloneDeep(app.data);
      if(app.data.image) {
        const form_data = new FormData();
        form_data.append('files', app.data.image);
        form_data.append('file_name', app.data.full_name || 'unknown_user');
        try {
          let res = await BackendApi.others.post({
            data: form_data,
            url: '/api/upload-user-img/'
          });
          res = res.data;
          req_data.image = res.upload_url;
        } catch (e) {
          this.show_confirm = true
          console.error(e);
          return;
        }
      }
      return BackendApi.generic.send({
        url: backend_url,
        method: this.method,
        data: req_data
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
.form-container {
  padding: 40px 0 40px 0;
}
</style>