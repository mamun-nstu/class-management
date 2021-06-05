<template>
  <div class="login">

    <div class="grid no-mobile">
      <div class="col-6 heading">NHST login</div>
      <Form
          class="grid no-mobile col-12"
          @submit="submit"
          v-slot="{ errors }"
          :validation-schema="schema"
          @input="error_msg=''"
      >
        <div class="col-12">
          <RequiredLabel label_for="login_username" value="Username"/>
          <Field
              id="login_username"
              name="username"
              type="email"
              placeholder="Enter your username"
              v-model="username"
          />
          <p class="error-msg">{{ errors.username }}</p>
        </div>
        <div class="col-12">
          <RequiredLabel label_for="login_password" value="Password"/>
          <Field
              v-model="password"
              v-slot="{field}"
              name="password"
          >
            <Password
                v-bind="field"
                placeholder="Enter password"
                id="login_password"
                name="password"
            />
          </Field>
          <p class="error-msg">{{ errors.password }}</p>
        </div>
        <div class="col-12 right-container">
          <span class="small-link" @click="$emit('forgot_password')">
            Forgot password?
          </span>

        </div>
        <p v-if="error_msg" class="col-12 error-msg text-center">
          {{ error_msg }}
        </p>
        <div class="col-12 center-container">
          <button :disabled="Object.keys(errors).length > 1" class="inverted">Login</button>
        </div>
        <div class="col-12" >
          <span class="small-link" @click="$emit('register')">
            Don't have an account? click to register
          </span>
        </div>
      </Form>
    </div>
  </div>
</template>

<script>
import ZephrApi from "../../js/zephr";
import {Form, Field} from "vee-validate";
import * as yup from "yup";
import Password from './elements/Password.vue';
import RequiredLabel from './elements/RequiredLabel.vue';
import loader_mixin from '../mixins/loader.js';
export default {
  name: "StudentForm",
  components: {
    Form,
    Field,
    Password,
    RequiredLabel,
  },
  mixins: [loader_mixin],
  methods: {
    submit: function () {
      const app = this;
      app.submitting = true;
      ZephrApi.login(this.username, this.password)
          .then((response) => {
            console.log(response);
            window.location.reload();
          })
          .catch((err) => {
            console.error(err);
            app.error_msg = 'Either username or password is invalid';
          }).finally(() => app.submitting = false);
    },
  },
  data: function () {
    return {
      schema: yup.object({
        username: yup.string().required('Username is required'),
        password: yup.string().required('Password is required'),
      }),
      username: "",
      password: "",
      error_msg: ""
    };
  },
};
</script>

