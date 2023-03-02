import { BButton } from "bootstrap-vue";

<template>
  <div class="about">
    <h1>Login</h1>

    <div>
      <b-form-group label="Entrar como:" v-slot="{ ariaDescribedby }">
        <b-form-radio
          v-model="selected"
          :aria-describedby="ariaDescribedby"
          name="empresa-radio"
          value="Empresa"
          @click="EmpresaCLick"
          >Empresa</b-form-radio
        >
        <b-form-radio
          v-model="selected"
          :aria-describedby="ariaDescribedby"
          name="cliente-radio"
          value="Cliente"
          @click="clienteClick"
          >Cliente</b-form-radio
        >
      </b-form-group>
    </div>

    <div>
      <h3>Escolha qual {{ selected }} quer entrar:</h3>
      <div>
        <b-dropdown id="dropdown-1" text="Pesquisar" class="m-md-2">
          <b-dropdown-item>First Action</b-dropdown-item>
          <b-dropdown-item>Second Action</b-dropdown-item>
          <b-dropdown-item>Third Action</b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item active>Active action</b-dropdown-item>
          <b-dropdown-item disabled>Disabled action</b-dropdown-item>
        </b-dropdown>
      </div>
      <BButton>Entrar</BButton>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: "",
    };
  },
  methods: {
    clienteClick() {
      console.log("Cliente");
    },

    empresaClick() {
      console.log("Empresa");
    },
  },
};
</script>
