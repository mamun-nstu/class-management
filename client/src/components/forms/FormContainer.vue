<template>
  <div class="form-container">
    <div class="d-flex flex-column">
      <ValidationObserver v-slot="{invalid, handleSubmit}" slim>
        <slot name="form"></slot>
        <v-alert
          v-model="show_confirm"
          border="left"
          close-text="Close Alert"
          :color="success? 'success': 'error'"
          dark
          dismissible
        > {{ success ? 'Success' : error_msg }}
        </v-alert>
        <div class="d-flex justify-center">
          <v-btn style="width: 250px" v-if="!view_only" class="btn-primary" @click="handleSubmit(submit)"> Submit
          </v-btn>
        </div>
      </ValidationObserver>
    </div>
  </div>
</template>

<script>
import { ValidationObserver } from 'vee-validate';
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
    },
    view_only: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  data: function () {
    return {
      show_confirm: false,
      success: false,
      error_msg: ''
    }
  },
  methods: {
    extract_error_msg(e) {
      if (e && e.response && e.response.data) {
        this.error_msg = e.response.data;
        if (typeof this.error_msg === 'object') {
          if (this.error_msg.username) {
            this.error_msg = 'Username is already taken';
          } else if (this.error_msg.student_id) {
            this.error_msg = 'Student ID is already taken';
          }
        }
      }
      if (this.error_msg.length > 500) {
        this.error_msg = 'Unknown error occurred';
      }
    },
    async submit() {
      console.log('Submitting to ' + this.url);
      const app = this;
      let backend_url = app.url;
      if (app.data.id) {
        backend_url = `${app.url}/${app.data.id}/`;
      }
      const req_data = _.cloneDeep(app.data);
      if (app.data.image) {
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
          this.show_confirm = true;
          this.extract_error_msg(e);
          console.error(e, e.response);
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
          window.location.reload();
        }).catch(e => {
          this.show_confirm = true;
          this.extract_error_msg(e);
          console.error(e, e.response);
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