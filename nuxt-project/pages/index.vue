<script setup>
  const config = useRuntimeConfig();
  const user = useUserStore()
  
  const { data: snippets, status, refresh } = useFetch(`${config.public.serverUrl}/snippets/`);
</script>

<template>
  <div class="text-center">
    <div class="container">
      <div class="row row-cols-4">
        <div v-if="user.userInfo!=null" class="col p-2">
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