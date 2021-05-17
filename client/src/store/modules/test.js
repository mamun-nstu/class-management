import {INCREMENT} from "../mutation_types";

const test_module = {
    state: () => {
     return {
         count: 0
     };
    },
    mutations: {
        [INCREMENT](state) {
            state.count += 1;
        }
    }
};
export default test_module;