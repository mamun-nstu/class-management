const user_mixin = {
  computed: {
    user() {
      return this.$store.state.user.data;
    },
  }
};

export default user_mixin;
