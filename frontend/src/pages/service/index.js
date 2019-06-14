import Taro, { Component } from '@tarojs/taro'
import { View, ScrollView, Text } from '@tarojs/components'
import { observer, inject } from '@tarojs/mobx'

import './index.less'


@inject('counterStore')
@observer
class Service extends Component {

  state = {
    serviceList: []
  }

  config = {
    navigationBarTitleText: '服务列表'
  }

  componentWillReact () {
    console.log('componentWillReact')
  }

  componentDidMount () {
    Taro.request({
      url: '/api/service/'
    }).then(({data}) => {
      this.setState({
        serviceList: data
      })
    })
  }

  render () {
    const { serviceList } = this.state;
    return (
      <View className='index'>
        <ScrollView>
          {
            serviceList.map(item => (
              <View>
                <Text>{item.name}</Text>
              </View>
            ))
          }
        </ScrollView>
      </View>
    )
  }
}

export default Service
