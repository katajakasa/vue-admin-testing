<template>
  <vuestic-navbar>
    <header-selector slot="selector" :isOpen.sync="valueProxy"/>
    <span slot="logo">
      <vuestic-icon-vuestic/>
    </span>

    <profile-dropdown class="col nav-item">
      <img src="https://i.imgur.com/nfa5itq.png"/>
    </profile-dropdown>
  </vuestic-navbar>

</template>

<script>
import VuesticIconVuestic from '../../../vuestic-theme/vuestic-components/vuestic-icon/VuesticIconVuestic'
import VuesticNavbar from '../../../vuestic-theme/vuestic-components/vuestic-navbar/VuesticNavbar'
import HeaderSelector from './components/HeaderSelector'
import ProfileDropdown from './components/dropdowns/ProfileDropdown'

export default {
  name: 'app-navbar',

  components: {
    VuesticIconVuestic,
    VuesticNavbar,
    HeaderSelector,
    ProfileDropdown
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    valueProxy: {
      get () {
        return this.isOpen
      },
      set (opened) {
        this.$emit('toggle-menu', opened)
      },
    },
  },
}
</script>
