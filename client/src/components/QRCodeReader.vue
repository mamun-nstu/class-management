<template>
  <div>
    <p class="error">{{ error }}</p>

    <p class="decode-result">Last result: <b>{{ result }}</b></p>
    <qrcode-stream :camera="camera" @decode="onDecode" :track="decorate" @init="onInit"/>
  </div>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader';

export default {
  name: 'QRCodeReader',
  components: { QrcodeStream },
  props: {
    camera: {
      type: String,
      default: 'auto',
      required: false
    }
  },
  data() {
    return {
      result: '',
      error: '',
    }
  },

  methods: {
    onDecode(result) {
      this.result = result;
      this.$emit('success', this.result);

    },
    decorate(detectedCodes, ctx) {
      for (const detectedCode of detectedCodes) {
        const { boundingBox: { x, y, width, height } } = detectedCode;

        ctx.lineWidth = 2;
        ctx.strokeStyle = '#007bff';
        ctx.strokeRect(x, y, width, height);
      }
    },

    async onInit(promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'NotAllowedError') {
          this.error = "You need to grant camera access permission"
        } else if (error.name === 'NotFoundError') {
          this.error = "No camera on this device"
        } else if (error.name === 'NotSupportedError') {
          this.error = "Secure context required (HTTPS, localhost)"
        } else if (error.name === 'NotReadableError') {
          this.error = "Is the camera already in use?"
        } else if (error.name === 'OverconstrainedError') {
          this.error = "Installed cameras are not suitable"
        } else if (error.name === 'StreamApiNotSupportedError') {
          this.error = "Stream API is not supported in this browser"
        } else if (error.name === 'InsecureContextError') {
          this.error = 'Camera access is only permitted in secure context. Use HTTPS or localhost rather than HTTP.';
        } else {
          this.error = `Camera error (${ error.name })`;
        }
        this.$emit('error', this.error);
      }
    }
  }
}
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>