<template>
  <div>

    <div class="row">
      <div class="col-md-12">
        <vuestic-widget :headerText="$t('tables.advanced')">
          <vuestic-data-table
            :apiUrl="apiUrl"
            :tableFields="tableFields"
            :itemsPerPage="itemsPerPage"
            :defaultPerPage="defaultTablePerPage"
            :sortFunctions="sortFunctions"
            :apiMode="apiMode"
            :paginationPath="paginationPath"
            :queryParams="queryParams"
          >
            <spring-spinner
              slot="loading"
              :animation-duration="2500"
              :size="70"
              color="#4ae387"
            />
          </vuestic-data-table>
        </vuestic-widget>
      </div>
    </div>

  </div>
</template>

<script>
import Vue from 'vue'
import { SpringSpinner } from 'epic-spinners'

export default {
  name: 'Table',
  components: {
    SpringSpinner
  },
  data () {
    return {
      apiUrl: 'http://localhost:9000/',
      apiMode: true,
      tableFields:  [
        {
          name: 'kek',
          sortField: 'kek',
          width: '24%'
        },
      ],
      itemsPerPage: [
        {
          value: 5
        },
        {
          value: 6
        },
        {
          value: 10
        }
      ],
      sortFunctions: {
        'kek': function (item1, item2) {
          return item1 >= item2 ? 1 : -1
        },
      },
      paginationPath: '',
      defaultTablePerPage: 6,
      queryParams: {
        sort: 'sort',
        page: 'page',
        perPage: 'per_page'
      }
    }
  }
}
</script>

<style lang="scss">

  .color-icon-label-table {
    td:first-child {
      width: 1rem;
    }
  }
</style>
