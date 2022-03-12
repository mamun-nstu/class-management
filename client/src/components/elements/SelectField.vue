<template>
  <ValidationProvider :rules="rules" v-slot="{errors}">
    <v-select
        v-bind="$attrs"
        v-on="$listeners"
    ></v-select>
    <p v-if="errors.length > 0" class="error"> {{ errors[0] }} </p>
  </ValidationProvider>
</template>

<script>
import {ValidationProvider} from 'vee-validate';

export default {
  name: "SelectField",
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
    rules: {
      type: Object,
      required: false,
      default: () => {}
    }
  },
}
</script>

<style scoped>

</style>