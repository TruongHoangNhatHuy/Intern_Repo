<script setup>
  const config = useRuntimeConfig();
  const user = useUserStore()
  
  const { data: snippets, status, refresh } = useFetch(`${config.public.serverUrl}/snippets/`);
</script>

<template>
  <div class="text-center">
    <div class="container">
      <!-- logged in index -->
      <div class="row row-cols-2 row-cols-md-4" v-if="user.userInfo!=null">
        <div class="col-12 col-md-12 mt-2">
          <h2>Your snippets</h2>
        </div>
        <div class="col p-2">
          <div class="btn btn-primary card h-100" @click="navigateTo(`/add`)">
            <div class="card-body">
              <h3 class="fw-normal fst-italic">Add snippet</h3>
            </div>
          </div>
        </div>
        <div class="col p-2" v-if="status==`success`" v-for="(item,index) in snippets.results.filter(x => x.owner==user.userInfo.username)" :key="index">
          <ItemCard 
            :title="item.title" 
            :content="'Language: '+item.language" 
            :description="'Owner: '+item.owner"
            @openDetail="navigateTo(`/detail/${item.id}`)"
          />
        </div>
        <div class="col-12 col-md-12 mt-2">
          <h2>Other snippets</h2>
        </div>
        <div class="col p-2" v-if="status==`success`" v-for="(item,index) in snippets.results.filter(x => x.owner!=user.userInfo.username)" :key="index">
          <ItemCard 
            :title="item.title" 
            :content="'Language: '+item.language" 
            :description="'Owner: '+item.owner"
            @openDetail="navigateTo(`/detail/${item.id}`)"
          />
        </div>
      </div>
      <!-- guest index -->
      <div class="row row-cols-2 row-cols-md-4" v-else>
        <div class="col p-2" v-if="status==`success`" v-for="(item,index) in snippets.results" :key="index">
          <ItemCard 
            :title="item.title" 
            :content="'Language: '+item.language" 
            :description="'Owner: '+item.owner"
            @openDetail="navigateTo(`/detail/${item.id}`)"
          />
        </div>
      </div>
    </div>
  </div>
</template>