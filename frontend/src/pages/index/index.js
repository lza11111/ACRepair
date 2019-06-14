import Taro, { Component } from '@tarojs/taro'
import { View, Button, Text } from '@tarojs/components'
import { observer, inject } from '@tarojs/mobx'

import './index.less'


@inject('counterStore')
@observer
class Index extends Component {

  config = {
    navigationBarTitleText: '首页'
  }

  componentWillMount () { }

  componentWillReact () {
    console.log('componentWillReact')
  }

  componentDidMount () { }

  gotoHome = () => {
    Taro.navigateTo({
      url: '/pages/home/index',
    })
  }

  gotoServiceList = () => {
    Taro.navigateTo({
      url: '/pages/service/index',
    })
  }

  gotoAppointment = () => {
    Taro.navigateTo({
      url: '/pages/appointment/index',
    })
  }

  render () {
    return (
      <View className='index'>
        <Button onClick={this.gotoHome}>公司简介</Button>
        <Button onClick={this.gotoServiceList}>服务列表</Button>
        <Button onClick={this.gotoAppointment}>我要预约</Button>
        <Button onClick={this.gotoSearch}>查询预约</Button>
      </View>
    )
  }
}

export default Index
