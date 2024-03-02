/*
 * mainpp.cpp
 *
 *  Created on: Jan 6, 2024
 *      Author: HP GAMING
 */

#include <mainpp.h>
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;

std_msgs::Int32MultiArray str_msg;
ros::Publisher chatter("chatter", &str_msg);

int32_t value[3] = {65535, -65535, 0};
extern int32_t incoming_value[3];

void messageCb(const std_msgs::Int32MultiArray& incoming_msg )
{
	incoming_value[0] = incoming_msg.data[0];
}
ros::Subscriber<std_msgs::Int32MultiArray> sub("talker", &messageCb );


void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart){
  nh.getHardware()->flush();
}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart){
  nh.getHardware()->reset_rbuf();
}

void setup(void)
{
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(sub);
}

void loop(void)
{
  HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);

  str_msg.data = value;
  str_msg.data_length = 3;
  chatter.publish(&str_msg);


  nh.spinOnce();
}
