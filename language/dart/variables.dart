void main() {
  variables();
  nullSafety();
  defaultValue();
}

void variables() {
  // Object name, String name
  // --> 타입 추론 가능
  var name = 'Duho Lee';
  print(name);
}

void nullSafety() {
  // Nullable type이므로 null을 선언할 수 있습니다.
  String? name1 = null;
  // Non-nullable type이므로 null을 선언할 수 없습니다.
  // String name2 = null;

  // 타입을 추론할 수는 없지만 runtime 시 Null type으로 선언됩니다.
  var name3 = null;

  print(name1.runtimeType);
  // print(name2);
  print(name3);
}

void defaultValue() {
  int? lineCount1;
  print(lineCount1); // null

  int lineCount2;
  // print(lineCount2); // Error

  lineCount2 = 0; // 선언 후 사용
  print(lineCount2); // 0
}
