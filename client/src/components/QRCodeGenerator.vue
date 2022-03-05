<template>
  <div>
    <qrcode-vue :id="id" :value="value" :size="size" :level="level" render-as="canvas" />
  </div>
</template>

<script>
import QrcodeVue from 'qrcode.vue';

export default {
  name: 'QRCodeGenerator',
  components: { QrcodeVue },
  props: {
    id: {
      type: String,
      required: false,
      default: 'qrcode'
    },
    value: {
      type: String,
      required: true
    },
    size: {
      type: Number,
      required: false,
      default: 300
    },
    level: {
      type: String,
      required: false,
      default: 'H'
    },
    margin: {
      type: Number,
      required: false,
      default: 0,
    }
  },
}
</script>
