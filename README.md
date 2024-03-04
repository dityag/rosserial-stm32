# How to set STM32 for rosserial communication protocol

## USART/UART Mode and Configuration
1. Select **USART/UART** `Mode` to be `Asynchronous`
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/d348b6c0-ddb4-4fea-a3df-e1fe35768c0f)

2. Change the
   - `Baud Rate` to `57600` `8 Bits`
   - `Data Direction` to `Receive and Transmit` (to make STM32 a publisher or subscriber)
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/5731d469-a642-41db-8695-0a532bbb3961)

3. Add **DMA Stream** to `UART_TX` and `UART_RX`                                             
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/b38a6ba5-9de7-45a2-b8a2-ee786b02e4d9)
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/5333c350-ab0e-4692-b598-03f2d1520c5c)

4. In **NVIC Settings** add `global interrupt` on `DMA Stream` and `UART`
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/e919781a-e5b8-4a22-a82a-df46b2826bf7)

## Workspace Setting
1. In your workspace `Right-click` -> `convert to c++`                           
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/017c5352-c394-4541-a8ac-33b2facec51d)

2. `Right-click` on your workspace -> `Properties` -> `C/C++ General` -> `File Types`
3. Select `File Types` to `Use project settings` -> New
4. Type **Pattern** *.h and **Type** C++ Header File
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/043657cf-2324-4150-b100-041723f67c7a)

## Edit the library for rosserial
1. Copy the files in the `inc` and `src` folders into your workspace folder

2. In the library `STM32Hardware.h` change it according to your **UART** address (in this case I used `huart1`). Change **rbuflen** (receive buffer length) and **tbuflen** (transmit buffer length) according to needs (I used **`512` bytes**)
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/c55632a9-a8b5-4edd-ad92-4136084a472e)

3. Don't forget to change the `INPUT_SIZE` and `OUTPUT_SIZE` in the `node_handle.h` library to the same size as those in the `STM32Hardware.h` library (I used **`512` bytes**)
![image](https://github.com/dityag/rosserial-stm32/assets/83180280/971eb8b5-4558-4355-9169-cd6fcde34596)

> [!NOTE]
> Check full tutorial rosserial-stm32 in my youtube video https://youtu.be/vymdZJrDH-s?si=PDv-SFLuDGMAbRJJ
