import {createStore} from "vuex";
import test_module from "./modules/test";

export default createStore({
    modules: {
        test_module
    }
})