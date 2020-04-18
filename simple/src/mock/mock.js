import Mock from 'mockjs'

Mock.mock(/getNewsList/,{
    'list|5':[{
        'url':'@url',
        'title':"@ctitle(5,20)"
    }]
})

Mock.mock(/getProductList/,{
    pc: {
        title: "pc产品",
        list: [{
                title: "@ctitle(4)",
                url: "@url"
              },
              {
                title: "@ctitle(4)",
                url: "@url"
              },
              {
                title: "@ctitle(4)",
                url: "@url",
                hot:'@boolean'
              },
              {
                title: "@ctitle(4)",
                url: "@url"
              }
        ]
      },
      app: {
        title: "手机应用类",
        last:true,
        list: [
            {
                title: "@ctitle(4)",
                url: "@url"
              },
              {
                title: "@ctitle(4)",
                url: "@url",
                hot:'@boolean'
              },
              {
                title: "@ctitle(4)",
                url: "@url",
                
              },
              {
                title: "@ctitle(4)",
                url: "@url",
                hot:'@boolean'
              }
        ]
      }
})

Mock.mock(/getBoardList/,[
    {
        title:"@ctitle(4)",
        desription:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        desription:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        desription:'@ctitle(8,12)',
        saleout:'@boolean'
    },
    {
        title:"@ctitle(4)",
        desription:'@ctitle(8,12)',
        saleout:'@boolean'
    },
])


export default Mock