<template>
  <ValidationProvider :rules="rules" v-slot="{errors}">
    <v-select
        v-bind="$attrs"
        v-on="$listeners"
    ></v-select>
    <p v-if="errors.length > 0" class="error-msg"> {{ errors[0] }} </p>
  </ValidationProvider>
</template>

<script>
import {ValidationProvider} from 'vee-validate';

export default {
  name: "SelectField",
  components: {
    ValidationProvider
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