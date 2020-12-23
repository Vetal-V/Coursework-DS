<template>
  <div class="EditMyAdvert">
    <div class="content">
      <div class="container">
        <div class="col col-md-6 offset-md-3 align-self-center">
          <h1 class="font-weight-bold border border-dark rounded-pill align-middle text-advert">Редагувати оголошення</h1>
        </div>
        <p class="text-danger">{{this.mess}}</p>
        <div class="row">
          <div class="col col-6">
            <h2>Категорія: <p class="text-danger reded">*</p> </h2>
          </div>
          <div class="col col-6">
            <h3>{{advert_detail.category.name}}</h3>
            <button class="btn btn-info"  type="submit"  @click="setchangeCategory()" ><h5>Змінити</h5></button>
            <select v-if="this.changeCategory" id="selectList" @click="ResetAdvAddinsh()" v-model="advert.category" class="form-control">
              <option></option>
              <option>Одяг</option>
              <option>Транспорт</option>
              <option>Запчастини до транспорту</option>
              <option>Нерухомість</option>
              <option>Дитячий світ</option>
              <option>Робота</option>
              <option>Тварини</option>
              <option>Дім і сад</option>
              <option>Електроніка</option>
              <option>Мода і стиль</option>
              <option>Хобі, відпочинок і спорт</option>
              <option>Віддам даром</option>
              <option>Бюро знахідок</option>
            </select>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Одяг'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Одяг'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Штани</option>
              <option>Взуття</option>
              <option>Сорочки</option>
              <option>Капелюхи</option>
              <option>Плаття</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Транспорт'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Транспорт'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Легкові автомобілі</option>
              <option>Грузові автомобілі</option>
              <option>Автобуси</option>
              <option>Мотоцикли</option>
              <option>Скутери</option>
              <option>Спецтехніка</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Нерухомість'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Нерухомість'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Квартири/кімнати</option>
              <option>Будинки</option>
              <option>Земельні ділянки</option>
              <option>Комерційна нерухомість</option>
              <option>Гаражі/парковки</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Дитячий світ'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Дитячий світ'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Дитячий одяг</option>
              <option>Дитяче взуття</option>
              <option>Дитячі коляски</option>
              <option>Дитяча мебель</option>
              <option>Іграшки</option>
              <option>Товари для школи</option>
              <option>Інші дитячі товари</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Робота'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== ''  && advert.category === 'Робота'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Торгівля/продажі/закупи</option>
              <option>Будівництво</option>
              <option>Управління персоналом</option>
              <option>Охорона</option>
              <option>Туризм/відпустки/розваги</option>
              <option>Культура</option>
              <option>Медицина</option>
              <option>Маркетинг/реклама</option>
              <option>Інші пропозиції</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Тварини'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Тварини'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Віддам в хороші руки</option>
              <option>Собаки</option>
              <option>Кішки</option>
              <option>Птахи</option>
              <option>Акваріумістика</option>
              <option>Гризуни</option>
              <option>Рептилії</option>
              <option>Сільськогосподарські тварини</option>
              <option>Інші тварини</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Дім і сад'" >
            <h3 class="under_category">Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Дім і сад'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Канцтовари</option>
              <option>Мебель</option>
              <option>Продукти харчування</option>
              <option>Сад/город</option>
              <option>Будівництво/ремонт</option>
              <option>Інструменти</option>
              <option>Посуда/кухонне приладдя</option>
              <option>Рослини</option>
              <option>Садовий інвентар</option>
            </select>
          </div>

          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Електроніка'" >
            <h3 class="under_category" >Підкатегорія: </h3>
          </div>
          <div class="col col-6" v-if="advert.category !== '' && advert.category === 'Електроніка'">
            <select v-model="advert.under_category" class="form-control">
              <option></option>
              <option>Телефони і аксесуари</option>
              <option>Комп'ютери/ноутбуки і комплектуючі</option>
              <option>Аудіотехніка</option>
              <option>Техніка для дому</option>
              <option>Інша електроніка</option>
            </select>
          </div>

          <div class="col col-12">
            <hr>
          </div>

          <div class="col col-6">
            <h2>Тип оголошення: <p class="text-danger reded">*</p> </h2>
          </div>
          <div class="col col-6">
            <h3>{{advert_detail.filters.name}}</h3>
            <button class="btn btn-info"  type="submit"  @click="setchangeFilter()" ><h5>Змінити</h5></button>
            <select v-if="this.changeFilter" v-model="advert.filter" class="form-control">
              <option>Купити</option>
              <option>Продати</option>
              <option>Обміняти</option>
              <option>Віддати</option>
              <option>Запропонувати</option>
            </select>
          </div>

          <div class="col col-12">
            <hr>
          </div>

          <div class="col col-6">
            <h2>Тема: <p class="text-danger reded">*</p> </h2>
          </div>
          <div class="col col-6">
            <h3>{{advert_detail.subject}}</h3>
            <button class="btn btn-info"  type="submit"  @click="setchangeSubject()" ><h5>Змінити</h5></button>
            <input v-if="this.changeSubject" class="col col-12" type="text" placeholder="Введіть заголовок оголошення" value="" v-model="advert.subject">
          </div>

          <div class="col col-12">
            <hr>
          </div>

          <div class="col col-6">
            <h2>Опис: <p class="text-danger reded">*</p> </h2>
          </div>
          <div class="col col-6">
            <h3>{{advert_detail.description}}</h3>
            <button class="btn btn-info"  type="submit"  @click="setchangeDescription()" ><h5>Змінити</h5></button>
            <textarea v-if="this.changeDescription" v-model="advert.description" placeholder="Введіть опис оголошення" rows="5" cols="80" class="col col-12 description form-control"></textarea>
          </div>

          <!-- <div class="col col-6">
            <h2>Фото:</h2>
          </div>
          <div class="col col-6">
            <label>Вибрати файл
              <input type="file" id="file" ref="file" v-on:change="handleFile1Upload()"/>
            </label>
            <label>Вибрати файл
              <input type="file" id="file" ref="file1" v-on:change="handleFile2Upload()"/>
            </label >
            <label>Вибрати файл
              <input type="file" id="file" ref="file2" v-on:change="handleFile3Upload()"/>
            </label>
            <label>Вибрати файл
              <input type="file" id="file" ref="file3" v-on:change="handleFile4Upload()"/>
            </label >
            <label>Вибрати файл
              <input type="file" id="file" ref="file4" v-on:change="handleFile5Upload()"/>
            </label>
          </div> -->

          <div class="col col-12">
            <hr>
          </div>

          <div class="col col-6">
            <h2>Ціна (грн.): <p class="text-danger reded">*</p> </h2>
          </div>
          <div class="col col-6">
            <h3>{{advert_detail.price}} <i class="fas fa-hryvnia"></i></h3>
            <button class="btn btn-info"  type="submit"  @click="setchangePrice()" ><h5>Змінити</h5></button>
            <div v-if="this.changePrice" class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas fa-hryvnia"></i></span>
              </div>
              <input type="text" class="form-control price"  v-model="advert.price" aria-label="Amount (to the nearest dollar)">
              <div class="input-group-append">
                <span class="input-group-text">.00</span>
              </div>
            </div>
          </div>

        </div>
        <div class="description-advert">
          <p class="text-danger reded">*</p> - обов'язкове поле.
        </div>
        <div class="row ">
          <div class="col col-4"></div>
          <div class="col col-6">
            <button class="btn btn-lg btn-primary" @click="CreateAdv()" type="submit"><h5>Підтвердити зміни</h5></button>
          </div>
          <div class="col col-2"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "EditMyAdvert",

    created() {
      //do something after creating vue instance
      this.loadAdvert(this.$route.params.slug)
    },

    data() {
      return {
        advert: {
          category: '',
          under_category: '',
          filter: '',
          description: '',
          subject: '',
          // photos1: '',
          // photos2: '',
          // photos3: '',
          // photos4: '',
          // photos5: '',
          price: '',
          categoryid: '',
          filterid: '',
        },
        mess: '',
        advert_detail: "",
        changeCategory: false,
        changeFilter: false,
        changeSubject: false,
        changePrice: false,
        changeDescription: false,
      }
    },
    methods: {
      setchangeCategory() {
        this.changeCategory = true;
      },
      setchangeFilter() {
        this.changeFilter = true;
      },
      setchangeSubject() {
        this.changeSubject = true;
      },
      setchangePrice() {
        this.changePrice = true;
      },
      setchangeDescription() {
        this.changeDescription = true;
      },
      loadAdvert(slug){
        $.ajax({
            url: this.$store.getters.get_url_server + slug,
            type: "GET",
            success: (response) => {
                this.advert_detail = response
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
      CreateAdv(){
        if(this.changeCategory) {
          if(this.advert.under_category == '' && this.advert.category == 'Одяг') {
            this.advert.categoryid = 3;
          } else if (this.advert.under_category === '' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 9;
          } else if (this.advert.under_category === '' && this.advert.category === 'Запчастини до транспорту'){
            this.advert.categoryid = 31;
          } else if (this.advert.under_category === '' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 17;
          } else if (this.advert.under_category === '' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 23;
          } else if (this.advert.under_category === '' && this.advert.category === 'Робота'){
            this.advert.categoryid = 32;
          } else if (this.advert.under_category === '' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 42;
          } else if (this.advert.under_category === '' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 53;
          } else if (this.advert.under_category === '' && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 63;
          } else if (this.advert.under_category === '' && this.advert.category === 'Мода і стиль'){
            this.advert.categoryid = 69;
          } else if (this.advert.under_category === '' && this.advert.category === 'Хобі, відпочинок і спорт'){
            this.advert.categoryid = 70;
          } else if (this.advert.under_category === '' && this.advert.category === 'Віддам даром'){
            this.advert.categoryid = 71;
          } else if (this.advert.under_category == 'Штани' && this.advert.category == 'Одяг'){
            this.advert.categoryid = 4;
          } else if (this.advert.under_category === 'Взуття' && this.advert.category === 'Одяг'){
            this.advert.categoryid = 5;
          } else if (this.advert.under_category === 'Сорочки' && this.advert.category === 'Одяг'){
            this.advert.categoryid = 6;
          } else if (this.advert.under_category === 'Капелюхи' && this.advert.category === 'Одяг'){
            this.advert.categoryid = 7;
          } else if (this.advert.under_category === 'Плаття' && this.advert.category === 'Одяг'){
            this.advert.categoryid = 8;
          } else if (this.advert.under_category === 'Легкові автомобілі' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 10;
          } else if (this.advert.under_category === 'Грузові автомобілі' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 11;
          } else if (this.advert.under_category === 'Автобуси' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 12;
          } else if (this.advert.under_category === 'Мотоцикли' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 13;
          } else if (this.advert.under_category === 'Скутери' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 14;
          } else if (this.advert.under_category === 'Спецтехніка' && this.advert.category === 'Транспорт'){
            this.advert.categoryid = 16;
          } else if (this.advert.under_category === 'Квартири/кімнати' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 18;
          } else if (this.advert.under_category === 'Будинки' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 19;
          } else if (this.advert.under_category === 'Земельні ділянки' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 20;
          } else if (this.advert.under_category === 'Комерційна нерухомість' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 21;
          } else if (this.advert.under_category === 'Гаражі/парковки' && this.advert.category === 'Нерухомість'){
            this.advert.categoryid = 22;
          } else if (this.advert.under_category === 'Дитячий одяг' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 24;
          } else if (this.advert.under_category === 'Дитяче взуття' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 25;
          } else if (this.advert.under_category === 'Дитячі коляски' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 26;
          } else if (this.advert.under_category === 'Дитяча мебель' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 27;
          } else if (this.advert.under_category === 'Іграшки' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 28;
          } else if (this.advert.under_category === 'Товари для школи' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 29;
          } else if (this.advert.under_category === 'Інші дитячі товари' && this.advert.category === 'Дитячий світ'){
            this.advert.categoryid = 30;
          } else if (this.advert.under_category === 'Торгівля/продажі/закупи' && this.advert.category === 'Робота'){
            this.advert.categoryid = 33;
          } else if (this.advert.under_category === 'Будівництво' && this.advert.category === 'Робота'){
            this.advert.categoryid = 34;
          } else if (this.advert.under_category === 'Управління персоналом' && this.advert.category === 'Робота'){
            this.advert.categoryid = 35;
          } else if (this.advert.under_category === 'Охорона' && this.advert.category === 'Робота'){
            this.advert.categoryid = 36;
          } else if (this.advert.under_category === 'Туризм/відпустки/розваги' && this.advert.category === 'Робота'){
            this.advert.categoryid = 37;
          } else if (this.advert.under_category === 'Культура' && this.advert.category === 'Робота'){
            this.advert.categoryid = 38;
          } else if (this.advert.under_category === 'Медицина' && this.advert.category === 'Робота'){
            this.advert.categoryid = 39;
          } else if (this.advert.under_category === 'Маркетинг/реклама' && this.advert.category === 'Робота'){
            this.advert.categoryid = 40;
          } else if (this.advert.under_category === 'Інші пропозиції' && this.advert.category === 'Робота'){
            this.advert.categoryid = 41;
          } else if (this.advert.under_category === 'Віддам в хороші руки' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 43;
          } else if (this.advert.under_category === 'Собаки' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 44;
          } else if (this.advert.under_category === 'Кішки' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 45;
          } else if (this.advert.under_category === 'Птахи' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 46;
          } else if (this.advert.under_category === 'Акваріумістика' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 47;
          } else if (this.advert.under_category === 'Гризуни' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 48;
          } else if (this.advert.under_category === 'Рептилії' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 49;
          } else if (this.advert.under_category === 'Сільськогосподарські тварини' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 50;
          } else if (this.advert.under_category === 'Інші тварини' && this.advert.category === 'Тварини'){
            this.advert.categoryid = 51;
          } else if (this.advert.under_category === 'Канцтовари' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 54;
          } else if (this.advert.under_category === 'Мебель' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 55;
          } else if (this.advert.under_category === 'Продукти харчування' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 56;
          } else if (this.advert.under_category === 'Сад/город' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 57;
          } else if (this.advert.under_category === 'Будівництво/ремонт' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 58;
          } else if (this.advert.under_category === 'Інструменти' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 59;
          } else if (this.advert.under_category === 'Посуда/кухонне приладдя' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 60;
          } else if (this.advert.under_category === 'Рослини' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 61;
          } else if (this.advert.under_category === 'Садовий інвентар' && this.advert.category === 'Дім і сад'){
            this.advert.categoryid = 62;
          } else if (this.advert.under_category === 'Телефони і аксесуари' && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 64;
          } else if (this.advert.under_category === "Комп'ютери/ноутбуки і комплектуючі" && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 65;
          } else if (this.advert.under_category === 'Аудіотехніка' && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 66;
          } else if (this.advert.under_category === 'Техніка для дому' && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 67;
          } else if (this.advert.under_category === 'Інша електроніка' && this.advert.category === 'Електроніка'){
            this.advert.categoryid = 68;
          } else {
            this.advert.categoryid = 100;
          }
        } else {
          this.advert.categoryid = this.advert_detail.category.id;
        }

        if(this.changeFilter) {
          if (this.advert.filter === 'Купити') {
            this.advert.filterid = 1;
          } else if (this.advert.filter === 'Продати') {
            this.advert.filterid = 2;
          } else if (this.advert.filter === 'Обміняти') {
            this.advert.filterid = 3;
          } else if (this.advert.filter === 'Віддати') {
            this.advert.filterid = 4;
          } else if (this.advert.filter === 'Запропонувати') {
            this.advert.filterid = 5;
          }
        } else {
          this.advert.filterid = this.advert_detail.filters.id;
        }
        if(!this.changeSubject){
          this.advert.subject = this.advert_detail.subject
        }
        if(!this.changeDescription){
          this.advert.description = this.advert_detail.description
        }
        if(!this.changePrice){
          this.advert.price = this.advert_detail.price
        }
        // let formData = new FormData();
        // if (this.advert.photos1 !== '') {
        //   formData.append('file', this.advert.photos1);
        // }
        // if (this.advert.photos2 !== '') {
        //   formData.append('file', this.advert.photos2);
        // }
        // if (this.advert.photos3 !== '') {
        //   formData.append('file', this.advert.photos3);
        // }
        // if (this.advert.photos4 !== '') {
        //   formData.append('file', this.advert.photos4);
        // }
        // if (this.advert.photos5 !== '') {
        //   formData.append('file', this.advert.photos5);
        // }

        if(this.advert.categoryid === '' || this.advert.filterid === '' || this.advert.subject === '' || this.advert.description === '' || this.advert.price === ''){
          this.mess = "Ви не заповнили обов'язкові поля. Будь-ласка, заповніть їх та спробуйте знову.";
          return;
        }

        $.ajax({
          url: this.$store.getters.get_url_server + "profile/update-advert/" + this.$route.params.id + "/",
          type: "PUT",

          data: {
              filters: this.advert.filterid,
              category: this.advert.categoryid,
              date: this.advert.termid,
              subject: this.advert.subject,
              description: this.advert.description,
              price: this.advert.price,
              date: "3"
          },
          success: (response) => {
              window.location = '/myadverts'
          },
          error: (response) => {
              this.mess = response.responseJSON
          }
        })
      },
      handleFile1Upload () {
        this.advert.photos1 = this.$refs.file.files[0];
      },
      handleFile2Upload () {
        this.advert.photos2 = this.$refs.file1.files[0];
      },
      handleFile3Upload () {
        this.advert.photos3 = this.$refs.file2.files[0];
      },
      handleFile4Upload () {
        this.advert.photos4 = this.$refs.file3.files[0];
      },
      handleFile5Upload () {
        this.advert.photos5 = this.$refs.file4.files[0];
      },
      ResetAdvAddinsh () {
        this.advert.under_category = ''
      }
    },
  }
</script>

<style scoped>
  #content {
    min-height: calc(100vh-131px-100px)
  }
  .text-advert {
    text-align: center;
    margin-top: 0.3rem;
    margin-bottom: 2rem;
  }
  .reded {
    display: inline-block;
    vertical-align: top;
  }
  .under_category {
    text-indent: 1.5em;
  }
  .description {
    margin-bottom: 1rem;
  }
  .form-control {
    margin-bottom: 10px;
  }
  .price {
    padding-top: 10px;
  }
</style>
