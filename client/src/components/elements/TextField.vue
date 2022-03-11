<template>
  <ValidationProvider :name="label" :rules="rules" v-slot="{errors}">
    <v-text-field
        color="#FFFFFF"
        class="white--text"
        dark
        :value="value"
        @input="update"
        @blur="do_nothing"
        :label="label"
        :placeholder="placeholder"
        outlined
    ></v-text-field>
    <p v-if="errors.length > 0" class="error"> {{ errors[0] }} </p>
  </ValidationProvider>
</template>

<script>
import {ValidationProvider} from 'vee-validate';

export default {
  name: "TextField",
  components: {
    ValidationProvider
  },
  methods: {
    update: function (val) {
      console.log('Here ', val);
      this.$emit("input", val);
    },
    do_nothing: function () {

    }
  },
  props: {
    label: {
      type: String,
      required: false,
      default: ''
    },
    placeholder: {
      type: String,
      required: false,
      default: ''
    },
    rules: {
      type: Object,
      required: false,
      default: () => {}
    },
    value: {
      type: String,
      required: false,
      default: ''
    }
  },
}
</script>

<style scoped>

</style>