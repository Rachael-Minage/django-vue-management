const routes=[
    {path:'/home',component:home},
    {path:'/employee',component:employees},
    {path:'/department',component:department}
]


const router=new VueRouter({
    routes
})

const app = new Vue({
    router,
    delimiters: ['[[', ']]'],
}).$mount('#app')