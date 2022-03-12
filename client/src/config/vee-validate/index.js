import { extend } from 'vee-validate';
import { required, email, min, max } from 'vee-validate/dist/rules';

extend('required', {
  ...required,
  message: 'This field is required'
});

extend('max', {
  ...max,
  message: 'Maximum {length} length'
});

extend('min', {
  ...min,
  message: 'Minimum {length} length'
});

extend('email', {
  ...email,
  message: 'Must be an email'
});
