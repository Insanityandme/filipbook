<template>
  <a class="item-container" href="[[ item.fields.link ]]">
    <div class="item">
      <img class="img" src="[[ item.fields.image ]]"/>
      <p class="title">[[ item.fields.title ]]</p>
      <p class="subtitle">[[ item.fields.subtitle ]]</p>
    </div>
  </a>
</template>

<script>
export default {

  name: 'Item',

  props: ['item']

}
</script>
