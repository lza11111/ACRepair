import Taro, { Component } from '@tarojs/taro'
import { View, Button, Picker, Input } from '@tarojs/components'
import { observer, inject } from '@tarojs/mobx'

import './index.less'


@inject('counterStore')
@observer
class Appointment extends Component {
  state = {
    param: {
      phone_number: null,
      address: null,
      service_type: null,
      required_time: null,
    }
  }
  config = {
    navigationBarTitleText: '预约'
  }

  setParam = (obj) => {
    const { param } = this.state;
    this.setState({
      param: {
        ...param,
        ...obj,
      }
    })
  }

  submit = () => {
    const { param } = this.state;
    console.log(param);
  }

  render() {
    const { param: { phone_number, address, service_type, required_time } } = this.state;
    return (
      <View className='index'>
        <View>
          手机号：
          <Input
            value={phone_number}
            onChange={e => this.setParam({ phone_number: e.target.value })}
          />
        </View>
        <View>
          地址：
          <Input
            value={address}
            onChange={e => this.setParam({ address: e.target.value })}
          />
        </View>
        <View>
          预约项目：
          <Input
            value={service_type}
            onChange={e => this.setParam({ service_type: e.target.value })}
          />
        </View>
        <View>
          <View>
            <Picker
              mode='date'
              onChange={e => this.setParam({ required_time: e.detail.value })}
            >
              <View className='picker'>
                预约时间：{required_time}
              </View>
            </Picker>
          </View>
        </View>
        <Button onClick={this.submit}>提交</Button>
      </View>
    )
  }
}

export default Appointment;
