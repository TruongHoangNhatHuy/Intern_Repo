<script setup>
  const { data: snippets, status, refresh } = useFetch('http://127.0.0.1:8000/snippets/')
</script>

<template>
  <div class="text-center">
    <div class="container">
      <div class="row row-cols-4">
        <div class="col p-2">
          <div class="btn btn-primary card h-100" @click="navigateTo(`/add`)">
            <div class="card-body">
              <h3 class="fw-normal fst-italic">Add snippet</h3>
            </div>
          </div>
        </div>
        <div class="col p-2" v-if="status==`success`" v-for="(item,index) in snippets.results" :key="index">
          <ItemCard 
            :title="item.title" 
            :content="item.language" 
            :description="'Owner: '+item.owner"
            @openDetail="navigateTo(`/detail/${item.id}`)"
          />
        </div>
      </div>
    </div>
  </div>
</template>