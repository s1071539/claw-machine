<style scoped>
.memeber_button{
  position: relative;
  top: 50px;
  right: -700px;
}
.search_div{
  width:40%; 
  margin:0 auto; 
  display:flex; 
  position:absolute;
  top:130px;
  left:800px;
}
.tabs_div{
  position: relative;
  left: 60px;
  top: 130px;
}
.product_div{
  position:absolute; 
  top:180px; 
  left:400px; 
  width:70%;
}
.manage_button{
  text-align:center;  
  vertical-align:middle; 
  margin-top: 5px;
}
</style>


<template>
  <div><!-- all page -->
    <img src="../assets/logo.png" style="position:absolute; top:30px; left:100px;">
    <span style="position:absolute; top:30px; right:200px;"><i class="el-icon-coin"></i>目前餘額：{{user_money}}$</span>
    <el-popover placement="bottom" trigger="click" width=300 title="信用卡儲值" ref="money_pop">
      <br>
      <el-form :model="recharge" label-width="80px">
        <el-form-item prop="number" label="卡號" >
          <el-input v-model="recharge.number" style="width:200px; display: block;" placeholder="請輸入卡號" type="text">
            <i class="el-icon-bank-card" slot="prefix"></i>
          </el-input>
        </el-form-item>
        <el-form-item prop="digtal3" label="後三碼" >
          <el-input v-model="recharge.digtal3" style="width:200px; display: block;" placeholder="請輸入後三碼"></el-input>
        </el-form-item>
        <div style="left: 20px; position: relative;">
          <el-row>
            <el-col :span="7"><el-radio v-model="recharge.money" label="50" border>50</el-radio></el-col>
            <el-col :span="7"><el-radio v-model="recharge.money" label="100" border>100</el-radio></el-col>
            <el-col :span="7"><el-radio v-model="recharge.money" label="200" border>200</el-radio></el-col>
          </el-row>
          <el-row>
            <el-col :span="7" style="margin-top: 10px;"><el-radio v-model="recharge.money" label="500" border>500</el-radio></el-col>
            <el-col :span="7" style="margin-top: 10px;"><el-radio v-model="recharge.money" label="750" border>750</el-radio></el-col>
            <el-col :span="7" style="margin-top: 10px;"><el-radio v-model="recharge.money" label="1000" border>1000</el-radio></el-col>
          </el-row>
        </div>
        <div style="text-align: right; margin-top: 20px">
          <el-button size="mini" type="text" @click="$refs['money_pop'].doClose()">取消</el-button>
          <el-button type="primary" size="mini" @click="set_user_money">确定</el-button>
        </div>
      </el-form>
      <el-link type="primary" slot="reference" style="position:absolute; top:30px; right:100px;">儲值<i class="el-icon-circle-plus"></i></el-link>
    </el-popover>
    
    <div> <!-- member button-->
      <el-popover trigger="hover" width="200" placement="bottom">
        <div><span>成員名稱: {{user}}</span></div>
        <div><el-button type="primary" icon="el-icon-setting" class="manage_button" @click="manage">後台管理</el-button></div>
        <div><el-button type="primary" icon="el-icon-switch-button" class="manage_button" @click="logout">登出</el-button></div>
        <el-button  class="memeber_button" slot="reference" icon="el-icon-s-custom"></el-button>
      </el-popover>
    </div>

    <div class="search_div"> <!-- search -->
      <el-input  style="width:300px" v-model="search_text" placeholder="请输入内容"></el-input>
      <el-button type="primary" icon="el-icon-search" circle @click="search"></el-button>
    </div>

    <div class="tabs_div"><!-- 分類表 -->
      <el-row >
        <el-col :span="3">
          <el-menu default-active="全部" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" @select="select_menu">
            <el-menu-item index="全部">
              <i class="el-icon-position"></i> <span slot="title">全部</span>
            </el-menu-item>
            <el-menu-item index="VT">
              <i class="el-icon-position"></i> <span slot="title">VT</span>
            </el-menu-item>
            <el-menu-item index="APEX">
              <i class="el-icon-position"></i> <span slot="title">APEX</span>
            </el-menu-item>
            <el-menu-item index="手機">
              <i class="el-icon-position"></i> <span slot="title">手機</span>
            </el-menu-item>
            <el-menu-item index="食物">
              <i class="el-icon-position"></i> <span slot="title">食物</span>
            </el-menu-item>
            <el-menu-item index="口罩">
              <i class="el-icon-position"></i> <span slot="title">口罩</span>
            </el-menu-item>
            <el-menu-item index="娃娃">
              <i class="el-icon-position"></i> <span slot="title">娃娃</span>
            </el-menu-item>
            <el-menu-item index="成人">
              <i class="el-icon-position"></i> <span slot="title">成人</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-row >
    </div>

    <div class="product_div"><!-- 商品 -->
      <el-table :data="table_data"  max-height="700" fit>
        <el-table-column align="center" width="300px">
          <template slot="header" slot-scope="scope">
            <div>商品</div>
          </template>
          <template slot-scope="scope">
            <img :src= "scope.row.url"  style="cursor:pointer; max-width: 300px;" @click="cell_click(scope.row)">
            <p>{{scope.row.name}}</p>
          </template>
        </el-table-column>


        <el-table-column align="center" label="價格" prop="price" sortable>
        </el-table-column>

        <el-table-column align="center" label="數量" prop="amount" sortable>
         
        </el-table-column>

        <el-table-column align="center" label="熱門度" prop="hot" sortable>

        </el-table-column>

        <el-table-column align="center" label="上架時間" prop="time" sortable>
        
        </el-table-column>
    
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Show_All',
  data () {
    return {
      user:"",
      user_money:"",
      search_text:"",
      product_data:[],
      table_data:[],
      recharge:{
        number:"",
        digtal3:"",
        money:"",
      }
    }
  },
  created () {
    if(sessionStorage["user"] != undefined){
      this.user = JSON.parse(sessionStorage["user"])

      this.axios.get('/get_all_product',{
      params:{
          user: this.user
        }
      }).then(response => {
        this.product_data = response.data
        this.axios.post('/get_all_product_url').then(response => { 
          for (let i in response.data){
            this.product_data[i]['url'] = response.data[i]
          }
          this.table_data = this.product_data
        })
      })

      this.axios.post("/get_all_user",{
      }).then((response)=>{
        let db_user = response.data.filter((item)=>{ return item['user'] == this.user});
        this.user_money = db_user[0]['setting'];
      });


    }
  },
  watch:{
  },
  methods: {
    manage(){
       this.$router.push({name: 'manage'});
    },
    logout(){
      sessionStorage.clear();
      this.$router.push('/login');
    },
    select_menu(index){
      switch (index){
        case '全部':
          this.table_data = this.product_data;
          break;
        case 'VT':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "VT"});
          break;
        case 'APEX':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "APEX"});
          break;
        case '手機':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "手機"});
          break;
        case '食物':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "食物"});
          break;
        case '口罩':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "口罩"});
          break;
        case '娃娃':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "娃娃"});
          break;
        case '成人':
          this.table_data = this.product_data.filter((item)=>{ return item['group'] == "成人"});
          break;
      }
    },
    cell_click(row){
      sessionStorage.setItem("play_info", JSON.stringify(row));
      this.$router.push({name: 'play'});
    },
    search(){
      this.table_data = this.product_data.filter((item)=>{ return(item['name'].includes(this.search_text))})
    },
    set_user_money(){
      this.axios.post('/set_user_money', {
        user:  this.user,
        money: this.recharge.money,
      }).then(response => {
        location.reload();
        this.$message("加值成功");
      })
    },

    
  },
}
</script>
