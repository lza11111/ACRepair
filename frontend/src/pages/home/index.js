import Taro, { Component } from '@tarojs/taro'
import { View, Button, Text } from '@tarojs/components'
import { observer, inject } from '@tarojs/mobx'

import './index.less'


@inject('counterStore')
@observer
class Home extends Component {
  state = {
    description: null,
  }

  config = {
    navigationBarTitleText: '公司简介'
  }

  componentDidMount () {
    Taro.request({
      url: '/api/home/overview'
    }).then(({data}) => {
      this.setState({
        description: data.description
      })
    })
  }

  render () {
    const { description } = this.state;

    return (
      <View className='index'>
        <Text>{description}</Text>
      </View>
    )
  }
}

export default Home;
