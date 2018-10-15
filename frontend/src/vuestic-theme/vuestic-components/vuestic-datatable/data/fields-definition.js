export default {
  tableFields: [
    {
      name: 'kek',
      sortField: 'kek',
      width: '24%'
    },
  ],
  sortFunctions: {
    'name': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    },
    'email': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    }
  }
}
