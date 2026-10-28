### Перевод статьи

**Снижение задержки в сетях IoT посредством развертывания периферийного
ИИ: сравнительное исследование**

***Авторы**: Чэнь Л., Патель Р., Волков С., Накамура К. (2025)*

***Журнал:** Journal of Edge Computing and IoT Systems, том 12, вып. 3,
с. 145--152*.

**Аннотация (краткая версия)**

В данном исследовании сравниваются подходы к выводу (инференсу) ИИ
исключительно в облаке, исключительно на периферии и гибридный подход с
целью снижения задержки в сетях Интернета вещей (IoT). Эксперименты на
50 узлах ESP32-S3 с использованием квантованной модели MobileNetV3
показали, что обработка исключительно на периферии сократила среднюю
задержку с 187,6 мс до 23,4 мс при сохранении точности (\~94%).
Гибридный подход продемонстрировал сбалансированный компромисс с
задержкой 61,2 мс и наименьшим энергопотреблением (12,3 мДж на один
вывод). Результаты подтверждают эффективность периферийного ИИ для
IoT-приложений с жесткими требованиями к задержке.

**Ключевые слова**: периферийный ИИ; сети IoT; снижение задержки;
граничные вычисления; гибридная архитектура; энергоэффективность.

**Введение (Introduction)**

Стремительное распространение устройств Интернета вещей (IoT) оказало
беспрецедентную нагрузку на централизованную облачную инфраструктуру. К
2026 году приблизительно 30 миллиардов подключенных устройств генерируют
непрерывные потоки данных с датчиков, значительная часть которых требует
обработки в реальном времени для таких сфер применения, как беспилотные
транспортные средства, промышленный мониторинг и интеллектуальное
здравоохранение. Традиционные облачно-ориентированные архитектуры вносят
сетевую задержку, способную превышать 200 мс, что неприемлемо для
критически зависимых от времени рабочих нагрузок. Периферийные
вычисления, приближающие обработку непосредственно к источнику данных,
предлагают перспективную альтернативу. В данном исследовании изучается,
обеспечивает ли развертывание облегченных моделей инференса ИИ
непосредственно на периферийных узлах существенное снижение сквозной
задержки по сравнению с облачной обработкой без потери точности вывода.

**Методы (Methods)**

Мы провели контролируемый эксперимент с использованием испытательного
стенда из 50 узлов IoT, оснащенных микроконтроллерами ESP32-S3, и
локального периферийного сервера на базе NVIDIA Jetson Orin Nano.
Оценивались три конфигурации вывода: (1) полная облачная обработка через
инстанс AWS EC2 (g5.xlarge), (2) вывод исключительно на периферии с
использованием TensorFlow Lite Micro на Jetson и (3) гибридный подход,
при котором первичная фильтрация осуществлялась на периферийном узле, а
сложный инференс делегировался в облако. Рабочая нагрузка состояла из
задач классификации изображений в реальном времени с применением
квантованной модели MobileNetV3. Каждая конфигурация тестировалась на
протяжении 1000 циклов инференса. Мы измеряли сквозную задержку (мс),
точность вывода (%) и энергопотребление на один вывод (мДж).
Статистическая значимость оценивалась с помощью парных t-критериев
Стьюдента при пороговом уровне значимости $p < 0,05$.

**Результаты (Results)**

Конфигурация с обработкой исключительно на периферии достигла средней
задержки 23,4 мс ($SD = 4,1$) по сравнению с 187,6 мс ($SD = 22,3$) для
облачного подхода и 61,2 мс ($SD = 8,7$) для гибридного подхода.
Различие между периферийным и облачным вариантами оказалось
статистически значимым ($p < 0,001$). Точность инференса оставалась
сопоставимой во всех конфигурациях: 94,2% (облако), 93,8% (периферия) и
94,0% (гибрид), без статистически значимой разницы ($p = 0,34$).
Энергопотребление на один вывод было минимальным при гибридном подходе
(12,3 мДж), в то время как обработка исключительно на периферии
потребовала 18,7 мДж, а исключительно в облаке 31,2 мДж (последнее
обусловлено накладными расходами на радиопередачу данных).

**Обсуждение (Discussion)**

Полученные результаты демонстрируют, что развертывание периферийного ИИ
сокращает задержку приблизительно на 87% по сравнению с облачной
обработкой при сохранении эквивалентной точности вывода. Этот вывод
согласуется с недавними исследованиями, подтверждающими, что
квантованные модели способны сохранять точность в пределах 1%
относительно их аналогов с вычислением полной точности. Гибридная
конфигурация представляет собой убедительный компромисс: задержка
сокращается на 67% по сравнению с чисто облачной обработкой, а
энергопотребление оказывается наименьшим из всех трех вариантов. Это
свидетельствует о том, что интеллектуальное разделение задач позволяет
оптимизировать как быстродействие, так и энергоэффективность. Тем не
менее периферийные узлы сталкиваются с аппаратными ограничениями: лимиты
по объему памяти и тепловыделению могут сдерживать сложность
используемых моделей. В будущих работах целесообразно исследовать
динамическое разбиение моделей, при котором конвейер инференса
адаптируется в режиме реального времени с учетом текущих условий сети и
нагрузки на узлы. Кроме того, отдельного внимания требуют аспекты
безопасности при распределении моделей ИИ по граничным устройствам,
поскольку каждый такой узел расширяет потенциальную поверхность атаки.

### 30 слов и выражений из текста статьи

1.  **Latency reduction**: снижение задержки (*"Latency reduction in IoT
    networks through edge AI deployment"*).
2.  **Edge AI deployment**: внедрение / развертывание искусственного
    интеллекта на периферийных устройствах (*"through edge AI
    deployment: A comparative study"*).
3.  **Comparative study**: сравнительное исследование (*"A comparative
    study"*).
4.  **Cloud-only approach**: подход с вычислениями исключительно в
    облаке (*"compares cloud-only, edge-only, and hybrid AI inference
    approaches"*).
5.  **Edge-only inference**: вывод (инференс) исключительно на
    периферийных устройствах (*"edge-only inference using TensorFlow
    Lite Micro"*).
6.  **Hybrid architecture / approach**: гибридная архитектура /
    гибридный подход (*"The hybrid approach offered a balanced
    trade-off"*).
7.  **Quantized model**: квантованная модель нейросети (*"with a
    quantized MobileNetV3 model"*).
8.  **Mean latency**: средняя задержка передачи или обработки (*"cut
    mean latency from 187.6 ms to 23.4 ms"*).
9.  **Balanced trade-off**: сбалансированный компромисс (*"offered a
    balanced trade-off with 61.2 ms latency"*).
10. **Energy consumption**: энергопотребление (*"the lowest energy
    consumption (12.3 mJ per inference)"*).
11. **Low-latency applications**: приложения с жесткими требованиями к
    низкой задержке (*"edge AI's effectiveness for low-latency IoT
    applications"*).
12. **Energy efficiency**: энергоэффективность (*"Keywords: energy
    efficiency"*).
13. **Rapid proliferation**: быстрое распространение / масштабный рост
    (*"The rapid proliferation of Internet of Things (IoT) devices"*).
14. **Centralized cloud infrastructure**: централизованная облачная
    инфраструктура (*"unprecedented strain on centralized cloud
    infrastructure"*).
15. **Continuous streams of sensor data**: непрерывные потоки данных с
    датчиков (*"generate continuous streams of sensor data"*).
16. **Real-time processing**: обработка в режиме реального времени
    (*"requires real-time processing for applications"*).
17. **Autonomous vehicles**: беспилотные (автономные) транспортные
    средства (*"such as autonomous vehicles, industrial monitoring"*).
18. **Cloud-centric architectures**: облачно-центричные архитектуры
    (*"Traditional cloud-centric architectures introduce network
    latency"*).
19. **Time-critical workloads**: рабочие задачи, критичные ко времени
    выполнения (*"unacceptable for time-critical workloads"*).
20. **Data source**: источник данных (*"brings computation closer to the
    data source"*).
21. **Lightweight AI inference models**: легковесные (облегченные)
    модели инференса ИИ (*"deploying lightweight AI inference models
    directly on edge nodes"*).
22. **End-to-end latency**: сквозная (полная) задержка (*"significantly
    reduces end-to-end latency"*).
23. **Controlled experiment**: контролируемый эксперимент (*"We
    conducted a controlled experiment"*).
24. **Testbed**: испытательный стенд / экспериментальная платформа
    (*"using a testbed of 50 IoT nodes"*).
25. **Offload to the cloud**: делегировать (выгружать) вычисления в
    облако (*"complex inference was offloaded to the cloud"*).
26. **Image classification tasks**: задачи классификации изображений
    (*"real-time image classification tasks"*).
27. **Statistical significance**: статистическая значимость
    (*"Statistical significance was assessed using paired t-tests"*).
28. **Radio transmission overhead**: накладные расходы на радиопередачу
    данных (*"due to radio transmission overhead"*).
29. **Full-precision counterparts**: полноточные аналоги моделей
    (*"within 1% of their full-precision counterparts"*).
30. **Compelling middle ground**: убедительное компромиссное
    (промежуточное) решение (*"The hybrid configuration offers a
    compelling middle ground"*).

### TASK 1

#### Step 1: Navigating and positioning a text using publication details

- **Name of the journal**: Journal of Edge Computing and IoT Systems.

- **The volume number of the journal**: 12.

- **The issue number of the volume**: 3.

- **The year of publication**: 2025.

- **The first and the last page numbers of the article**: 145--152.

- **The title of the article**: Latency reduction in IoT networks
  through edge AI deployment: A comparative study.

- **The names (surnames and initials) of the authors**: Chen, L., Patel,
  R., Volkov, S., and Nakamura, K.

#### **Step 2: Genre, audience, and purpose**

##### **1. What type of article is this?**

- It is an original research article, as it presents the methodology,
  empirical findings, and statistical analysis of a controlled
  experimental study conducted on a physical hardware testbed.

##### **2. Who do you think it is written for?**

- Researchers, university lecturers, and professors, as well as graduate
  students specializing in embedded systems, edge computing, and applied
  machine learning for IoT.

- Experts in edge computing and IoT architectures, since the text
  assumes domain-specific technical literacy regarding microcontroller
  deployment, framework optimization, and neural network quantization.

##### **3. Questions based on the title:**

- **Why has the article been written?** The paper was written to
  investigate and experimentally evaluate whether moving machine
  learning inference to edge devices effectively mitigates severe
  network latency inherent to traditional cloud infrastructures in IoT
  systems.

- **What is the object of the article?** The object of the study is the
  comparative performance (specifically latency, accuracy, and energy
  consumption) of three AI inference paradigms: cloud-only, edge-only,
  and hybrid architectures within wireless IoT networks.

- **What does the article review / investigate?** The article
  investigates the trade-offs in end-to-end latency, model accuracy, and
  energy expenditure when deploying a quantized MobileNetV3 neural
  network across ESP32-S3 sensor nodes and a local edge accelerator.

#### **Step 3: Study the whole text and answer the questions**

##### **a. What is the background and aim of the investigation?**

- **Background**: The exponential proliferation of IoT devices generates
  immense volumes of telemetry data requiring real-time processing.
  Traditional centralized cloud architectures introduce network delays
  exceeding 200 ms, which is unacceptable for latency-sensitive
  applications like autonomous driving, smart healthcare, and industrial
  automation.

- **Aim**: To determine whether deploying lightweight AI inference
  models directly onto local edge nodes significantly reduces end-to-end
  latency compared to centralized cloud processing without degrading
  classification accuracy.

##### **b. What was done in the investigation?**

- The authors set up an experimental testbed comprising 50 IoT nodes
  powered by ESP32-S3 microcontrollers and an NVIDIA Jetson Orin Nano
  edge server.

- They evaluated three distinct inference deployment pipelines: full
  cloud computing via AWS EC2 (g5.xlarge), edge-only inference using
  TensorFlow Lite Micro, and a hybrid scheme where edge nodes filtered
  incoming inputs before offloading complex tasks to the cloud.

- They executed 1,000 cycles of real-time image classification using a
  quantized MobileNetV3 model, quantitatively recording end-to-end
  latency (ms), inference accuracy (%), and energy consumption per
  inference (mJ), validated through paired t-tests ($p < 0.05$).

##### **c.What was found/discovered?**

- Edge-only processing achieved a mean latency of 23.4 ms ($SD = 4.1$),
  slashing response time by roughly 87% compared to cloud-only
  processing (187.6 ms, $SD = 22.3$), a result proven statistically
  significant ($p < 0.001$).

- Inference accuracy remained virtually identical across all
  configurations: 94.2% for cloud, 93.8% for edge, and 94.0% for hybrid
  ($p = 0.34$).

- The hybrid model proved to be the most energy-efficient setup,
  consuming only 12.3 mJ per inference (versus 18.7 mJ on edge and 31.2
  mJ on cloud) due to the substantial reduction in wireless radio
  transmission overhead.

##### **d. What do the Results mean?**

- The results substantiate that local edge AI inference successfully
  resolves transmission latency bottlenecks in mission-critical IoT
  systems while preserving analytical precision.

- In addition, the findings demonstrate that a hybrid architecture
  serves as the most viable design compromise for battery-constrained
  remote devices requiring both low latency and minimal energy draw.

##### **e. What literature sources are referenced in the paper?**

- The paper references contemporary studies focused on model compression
  and post-training quantization, which corroborate that quantized
  neural networks retain predictive accuracy within 1% of their
  full-precision floating-point counterparts.


### TASK 2: Annotation (Humanized / De-AI Version)

**Title:** Annotation of the research article *"Latency reduction in IoT networks through edge AI deployment: A comparative study"*

The article I'm going to give a review of is taken from the *Journal of Edge Computing and IoT Systems* (Vol. 12, Issue 3, 2025, pp. 145–152). The headline of the article is *"Latency reduction in IoT networks through edge AI deployment: A comparative study"*. It is written by L. Chen, R. Patel, S. Volkov, and K. Nakamura. The article under discussion is an experimental study evaluating edge computing architectures for deep neural network inference in wireless sensor environments.

The topic of the article is latency reduction and energy consumption in IoT networks using local edge AI inference. The key issue of the article is the comparative performance of cloud-only, edge-only, and hybrid computing architectures. The article under discussion is devoted to the problem of network latency in centralized cloud systems, which often exceeds 200 ms and makes real-time workloads impractical for autonomous systems and industrial monitoring. The article under discussion may be divided into several logically connected parts which are the Introduction, Methods, Results, Discussion, and References.

The author starts by telling the reader that continuous sensor streams from billions of connected devices place heavy strain on centralized cloud data centers. At the beginning of the article the author describes the rationale for moving inference workloads directly to network edge nodes to avoid round-trip network delays while preserving model accuracy. Then the author explains the experimental methodology, tested on 50 ESP32-S3 microcontroller nodes linked to an NVIDIA Jetson Orin Nano edge server and an AWS EC2 cloud instance running a quantized MobileNetV3 model over 1,000 inference cycles. After that the author points out that edge-only processing dropped mean latency from 187.6 ms to 23.4 ms (an 87% reduction) while maintaining 93.8% accuracy, compared to 94.2% in the cloud. The author also touches upon the hybrid approach, which consumed 12.3 mJ per inference (the lowest among all three setups) because it reduced radio transmission overhead. In conclusion the author makes it clear that edge AI effectively resolves communication bottlenecks in latency-sensitive IoT systems. The author concludes by saying that future work should focus on dynamic model partitioning and address security risks on distributed edge devices.

---

### TASK 3: Oral Presentation (Humanized / De-AI Version)

**Speaker:** Dmitry Dolzhikov  
**Topic:** Latency Reduction in IoT Networks Through Edge AI Deployment  
**Estimated Speech Duration:** 5–7 minutes (~710 words)

```text
Timing Overview:
- 1. Opening: ~1.5 min (175 words)
- 2. Body:    ~4.0 min (400 words)
- 3. Closing: ~1.0 min (135 words)
Total: ~6.0 minutes at 120–130 words/min (710 words)
```

#### 1. Opening (~1.5 minutes)

Good afternoon, everyone. Thank you for being here today.

My name is Dmitry Dolzhikov. Today I am going to talk about reducing latency in IoT networks through edge AI deployment. My purpose is to look at how running lightweight machine learning models directly on local hardware can replace remote cloud processing for time-sensitive workloads, drawing on an empirical study published by Dr. Chen and his colleagues.

This issue is practical and immediate. In systems like automated manufacturing, connected medical devices, and self-driving transport, decisions must happen in tens of milliseconds. Relying on remote cloud servers across wide-area networks introduces communication delays that are simply too large for safety-critical tasks.

Here is the route map for today's presentation:
- To start with, I will outline the problem with traditional cloud-centric IoT architecture.
- Then I will walk through the experimental testbed and methodology used in the study.
- Next, I will review the comparative findings on latency, model accuracy, and power consumption.
- Finally, I will summarize what these results mean for system design and touch on future work.

#### 2. Body (~4.0 minutes)

Let us begin with the operational context. Industry estimates project around 30 billion connected devices in use, producing continuous telemetry that requires fast interpretation.

In a conventional cloud-centric pipeline, raw sensor readings travel over multiple network hops to a data center, get processed, and travel back. This round trip routinely exceeds 200 milliseconds. To put that in perspective, an autonomous vehicle traveling at 100 kilometers per hour covers roughly 5.5 meters in 200 milliseconds before receiving an inference result. For emergency braking or obstacle avoidance, that delay is hazardous. Moving the model onto local edge hardware removes the round trip entirely.

Now we can move on to the experimental setup. The authors evaluated three system configurations:
1. First, full cloud processing using an AWS EC2 instance.
2. Second, edge-only inference using TensorFlow Lite Micro on an NVIDIA Jetson Orin Nano edge server paired with ESP32-S3 sensor nodes.
3. Third, a hybrid scheme where sensor nodes run preliminary filtering locally and forward only complex frames to the cloud.

All three configurations ran real-time image classification with a quantized MobileNetV3 model over 1,000 test cycles.

Turning now to the experimental findings, the data highlights three specific metrics.

First, on end-to-end latency: the edge-only architecture reached an average response time of 23.4 milliseconds, compared to 187.6 milliseconds in the cloud. That is an 87 percent reduction, and the paired t-test confirmed the difference is statistically significant at p below 0.001.

Second, regarding classification accuracy: engineers often worry that 8-bit integer quantization will degrade accuracy. Here, the cloud model scored 94.2 percent, the edge model reached 93.8 percent, and the hybrid setup scored 94.0 percent. With a p-value of 0.34, the accuracy differences were negligible.

Third, regarding energy consumption: the hybrid architecture was the most efficient, using 12.3 millijoules per inference, compared to 18.7 millijoules on the edge and 31.2 millijoules in the cloud. The explanation is straightforward: radio transmission draws significant battery power on remote sensors, so running local filtering and reducing transmission volume saves more energy than computing entirely on the edge or sending every raw frame over the air.

That covers the core experimental results and the performance differences between the three architectures.

#### 3. Closing (~1.0 minute)

In conclusion, let me summarize the main takeaways.

Edge-only processing cuts response latency by 87 percent while retaining model accuracy within half a percentage point of cloud baselines. When energy constraints are tight, a hybrid pipeline provides the best balance between fast response and low battery drain.

Looking ahead, engineers still need to address hardware bottlenecks such as thermal dissipation and on-chip memory limits, along with security risks that come from distributing models across exposed hardware.

The practical takeaway is straightforward: edge AI gives us a reliable way to meet sub-30-millisecond latency targets on embedded hardware today without compromising accuracy.

Thank you very much for your attention.

I will now be glad to answer any questions you have.
