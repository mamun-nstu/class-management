import {UPDATE_BATCHES} from "../store/mutation_types";

const batch_mixin = {
  created() {
    return this.$store.dispatch(UPDATE_BATCHES);
  },
  computed: {
    batches() {
      return this.$store.state.batches.data;
    },
  }
};

export default batch_mixin;
